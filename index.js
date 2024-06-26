const decomment = require("decomment");
var fs = require('fs');

var filename = process.argv[2];
var code = fs.readFileSync(filename, {encoding: 'utf8'});
fs.writeFileSync('out.js', decomment(code));
