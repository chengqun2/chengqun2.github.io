const obj = {
    "Student Origial Calendar": "['recPmudclSZnWB3gL']",
    "New Student ID": "recPmudclSZnWB3gL"
}

{{ 
    (
      $json["Student"] 
        ? (Array.isArray($json["Student"]) ? $json["Student"] : JSON.parse($json["Student"]))
        : []
    ).concat(
      $('Webhook').item.json.query.recordID
        ? (Array.isArray($('Webhook').item.json.query.recordID) ? $('Webhook').item.json.query.recordID: [$('Webhook').item.json.query.recordID])
        : []
    )
}}


{{
    (
        $json["Student"] 
        ? (Array.isArray($json["Student"]) ? $json["Student"] : JSON.parse($json["Student"]))
        : []
    ).filter(item => 
        !($('Webhook').item.json.query.recordID 
        ? (Array.isArray($('Webhook').item.json.query.recordID) 
            ? $('Webhook').item.json.query.recordID.includes(item) 
            : item === $('Webhook').item.json.query.recordID)
        : false)
    )
}}


{{
    (
        $json["Student"] 
        ? (Array.isArray($json["Student"]) ? $json["Student"] : JSON.parse($json["Student"]))
        : []
    ).filter(item => 
        !($('get records from Enrolled').item.json['Lead and Trial'][0]
        ? (Array.isArray($('get records from Enrolled').item.json['Lead and Trial'][0]) 
            ? $('get records from Enrolled').item.json['Lead and Trial'][0].includes(item) 
            : item === $('get records from Enrolled').item.json['Lead and Trial'][0])
        : false)
    )
}}

