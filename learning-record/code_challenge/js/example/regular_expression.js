// const url = "https://drive.google.com/file/d/1DeJc69aBfoWMkvhwrMjpqDVU1hjaluqd/view?usp=sharing";
// // match all the `a-zA-Z0-9_-` after /d/
// const match = url.match(/\/d\/([a-zA-Z0-9_-]+)/);
// // Outputs: 1DeJc69aBfoWMkvhwrMjpqDVU1hjaluqd
// console.log(match[1]); 


const studentName = "Faiq Iman bin Mukhlis"
if(studentName.startsWith("#")){
    const match = studentName.match(/([#0-9a-zA-Z]+)/)
    if (match) {
        const nameWithoutStudentId = studentName.substring(match[1].length).trim()
        console.log('[' + nameWithoutStudentId + ']')
    } else {
        console.log('No match found')
    }
}else{
    console.log(studentName)
}

