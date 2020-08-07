
// Author: https://github.com/douglascarlini

const http = require('http')

var server = http.createServer()

server.addListener('request', (req, res) => {

    req.on('end', () => {

        res.writeHead(200)
        res.write("OK")
        res.end()

    })

})

server.listen(8080)
