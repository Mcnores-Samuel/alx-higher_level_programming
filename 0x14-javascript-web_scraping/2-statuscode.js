#!/usr/bin/node
/*display the status code of a GET request */
const url = process.argv.slice(2)[0];
const request = require("request");
request.get(url, (error, response) => {
    console.log('code: ', response.statusCode)
})
