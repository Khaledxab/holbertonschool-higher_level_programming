#!/usr/bin/node
const c = require('fs');
const args = process.argv;
const a = c.readFileSync(args[2], 'utf-8');
const b = c.readFileSync(args[3], 'utf-8');
c.writeFileSync(args[4], a + b);