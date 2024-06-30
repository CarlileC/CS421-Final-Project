const express = require('express') // require express to be downloaded
const app = express() // create an instance of an express app
const port = 3000 // define the port number that the local server will be running on

app.get('/', (req, res) => {
    res.send('Hello coffee and friends!')
})

app.listen(port, () => {
    console.log (`Example app listening on port ${port}`)
})