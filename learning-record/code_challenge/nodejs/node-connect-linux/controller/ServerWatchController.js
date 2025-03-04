const { Client } = require('ssh2');

module.exports = {
    ServerOperate: (req, res) => {
        const key = req.body.key
        if ('Ernest' !== key) {
            return res.status(200).json('Wrong key!')
        }
        const command = req.body.command
        if (command.indexOf('rm') > -1) {
            return res.status(200).json('Wrong command!')
        }
        const serverConfig = req.body.serverConfig
        executeCommand(command, serverConfig).then(function (data) {
            res.status(200).json(data);
        }).catch(error => {
            res.status(500).json(error)
        });
    }
}

function executeCommand(command, serverConfig) {
    return new Promise((resolve, reject) => {
        const conn = new Client();
        try{
            conn.on('ready', () => {
                conn.exec(command, (err, stream) => {
                    if (err) throw err;
                    stream.on('data', (data) => {
                        resolve(`${data}`);
                    }).on('close', (code, signal) => {
                        conn.end();
                    }).stderr.on('data', (data) => {
                        console.log(`STDERR: ${data}`);
                        reject(`STDERR: ${data}`);
                    });
                });
            }).connect(serverConfig);
        }catch(error){
            console.error(error);
        }
    });
}
