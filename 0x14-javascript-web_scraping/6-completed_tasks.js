#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
let todos;
const doneTasks = {};
r.get(url, (err, response, body) => {
  (err) ? console.log(err) : todos = JSON.parse(body);
  for (const i in todos) {
    const todo = todos[i];
    if (todo.completed === true) {
      if (!doneTasks[todo.userId]) {
        doneTasks[todo.userId] = 1;
      } else {
        doneTasks[todo.userId]++;
      }
    }
  }
  console.log(doneTasks);
});
