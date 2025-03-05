import subprocess
import sys
from flask import Flask, json, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Replace with your actual API endpoint and API key
base_url = "http://127.0.0.1:8088/v1"

app = Flask(__name__)

# 配置数据库连接信息
# 请将 username、password、localhost 和 dbname 替换为你自己的信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jsfr123456@127.0.0.1:7082/dify_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建SQLAlchemy实例
db = SQLAlchemy(app)

# ChatHistory
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(4000), nullable=False)
    user = db.Column(db.String(255), nullable=False)
    conversation_id = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    def __repr__(self):
        return f'<ChatHistory {self.id}>'

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('query','')
    conversation_id = request.json.get('conversation_id', '') 
    print('query=>', query, ', conversation_id=>',conversation_id)
    api_url = base_url + "/chat-messages"
    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "conversation_id": conversation_id,
        "user": "Ernest710"
    }
    # The api_key belongs to a workflow or a chatflow
    api_key = request.json.get('api_key','app-h5HAMxK3x0mIcqpNct8Lq2p8')

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # Set timeout to 3 minutes in seconds
    response = requests.post(api_url, headers=headers, json=data, timeout=180)
    if response.status_code == 200:
        conversation_id = response.json()['conversation_id']
        # 创建一个新的 ChatHistory 对象
        new_book = ChatHistory(message=query, 
                               user='Ernest', 
                               conversation_id=conversation_id,
                               create_time=db.func.now()
                               )
        # 将新的 ChatHistory 对象添加到数据库会话中
        db.session.add(new_book)
        # 提交会话，将更改保存到数据库
        db.session.commit()
        print("Success:", response.json())
        return jsonify({"result": response.json()})
    else:
        print("Error:", response.status_code, response.text)
        return jsonify({"result": response.status_code}), 201


@app.route('/getChatHistory', methods=['GET'])
def getChatHistory():
    # Get user from query parameters instead of JSON body
    user = request.args.get('user', 'Ernest')  # Default to 'Ernest' if not provided
    conversation_id = request.args.get('conversation_id')  # Can be None
    # print('conversation_id=>',conversation_id)
    query = ChatHistory.query.filter_by(user=user)
    # Get pagination parameters from query parameters
    page_no = int(request.args.get('pageNo', 1))  # Default to page 1
    page_size = int(request.args.get('pageSize', 10))  # Default to 10 items per page
    
    if conversation_id:
        query = query.filter_by(conversation_id=conversation_id)
    else:
        subquery = db.session.query(
            ChatHistory.conversation_id,
            db.func.min(ChatHistory.id).label('min_id')
        ).group_by(ChatHistory.conversation_id).subquery()

        query = query.join(
            subquery,
            ChatHistory.conversation_id == subquery.c.conversation_id
        ).filter(ChatHistory.id == subquery.c.min_id)
        
    # Apply pagination
    paginated_query = query.order_by(ChatHistory.id.desc()).paginate(
        page=page_no, per_page=page_size, error_out=False)
    # Convert the results to a list of dictionaries
    history_list = [{'message': ch.message, 
                     'conversation_id': ch.conversation_id,
                     'create_time': ch.create_time,
                     'create_time_format': ch.create_time.strftime('%Y-%m-%d %H:%M:%S')
                    } 
                   for ch in paginated_query.items]
    # print('history_list:',history_list)
    return jsonify({"chat_history": history_list})


@app.route('/chatStream', methods=['POST'])
def chatStream():
    user = request.json.get('user', 'Ernest')
    query = request.json.get('query', '')
    # inputs = request.json.get('inputs', '')
    inputs = {}
    conversation_id = request.json.get('conversation_id', '')
    # The api_key belongs to a workflow or a chatflow
    api_key = 'app-h5HAMxK3x0mIcqpNct8Lq2p8'
    # Get api_key and inputs from flow_properties table
    # try:
    #     result = db.session.execute(
    #         text("SELECT api_key, inputs FROM flow_properties WHERE user = :user"), 
    #         {"user": user}
    #     ).first()
    #     if result:
    #         api_key = result.api_key or api_key  # Use provided value as fallback
    #         inputs = result.inputs or inputs  # Use provided value as fallback
    #         inputs = inputs.strip()
    #         print('api_key,', api_key, 'inputs,', inputs)
    # except Exception as e:
    #     print(f"Error fetching properties: {e}")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    api_url = base_url + "/chat-messages"
    request_data = {
        "inputs": inputs,
        "query": query,
        "response_mode": "streaming",
        "conversation_id": conversation_id,
        "user": user
    }

    def generate():
        final_conversation_id = conversation_id
        response = requests.post(api_url, headers=headers, json=request_data, stream=True)
        response.timeout = 180  # 3 minutes in seconds
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data:'):
                    stream_data = line.split('data:', 1)[1].strip()
                    if stream_data:
                        try:
                            parsed_data = json.loads(stream_data)
                            if parsed_data.get('conversation_id'):
                                final_conversation_id = parsed_data['conversation_id']
                        except json.JSONDecodeError:
                            pass
                        yield f"data: {stream_data}\n\n"

        # Save chat history after streaming is complete, within the app context
        with app.app_context():
            try:
                new_chat_history = ChatHistory(
                    message=query,
                    user='Ernest',
                    conversation_id=final_conversation_id,
                    create_time=db.func.now()
                )
                db.session.add(new_chat_history)
                db.session.commit()
            except Exception as e:
                print(f"Error saving chat history: {e}")
                db.session.rollback()

    return app.response_class(generate(), mimetype='text/event-stream')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    user = request.form.get('user', 'default_user')
    
    # The api_key belongs to a workflow or a chatflow
    api_key = request.form.get('api_key','app-h5HAMxK3x0mIcqpNct8Lq2p8')

    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    # Forward the file to Dify API
    files = {'file': (file.filename, file.stream, file.content_type)}
    upload_url = base_url + '/files/upload'
    
    try:
        response = requests.post(upload_url, headers={'Authorization': headers['Authorization']}, files=files, data={'user': user})
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/saveFlowProperties', methods=['POST'])
def save_flow_properties():
    try:
        user = request.json.get('user', 'Ernest')
        inputs = request.json.get('inputs')
        # Update existing flow_properties record for the user
        stmt = text("UPDATE flow_properties SET inputs = :inputs WHERE user = :user")
        # Convert inputs to string if it's not already
        if inputs is not None:
            inputs = json.dumps(inputs)
        db.session.execute(stmt, {'inputs': inputs, 'user': user})
        db.session.commit()
        return jsonify({'message': 'Flow properties saved successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

def get_mac_address(ip):
    if sys.platform.startswith('win'):
        try:
            result = subprocess.run(['arp', '-a', ip], capture_output=True, text=True, check=True)
            output = result.stdout
            lines = output.splitlines()
            for line in lines:
                if ip in line:
                    parts = line.split()
                    return parts[1]
            return None
        except subprocess.CalledProcessError:
            return None
    elif sys.platform.startswith('linux'):
        try:
            result = subprocess.run(['ip', 'neigh', 'show', ip], capture_output=True, text=True, check=True)
            output = result.stdout
            parts = output.split()
            if len(parts) > 4 and parts[4] != 'FAILED':
                return parts[4]
            return None
        except subprocess.CalledProcessError:
            return None
    return None

@app.route('/getMacAddress')
def getMacAddress():
    client_ip = request.remote_addr
    mac_address = get_mac_address(client_ip)
    result = {}
    result['client_ip'] = client_ip
    result['mac_address'] = mac_address
    return result

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run()
