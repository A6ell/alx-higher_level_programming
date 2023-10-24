#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `HTTP Status Code ${response.statusCode}`);
    process.exit(1);
  } else {
    const todos = JSON.parse(body);

    // Initialize an object to store the completed task counts for each user
    const completedTasksByUser = {};

    // Iterate through the todos to count completed tasks by user
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
