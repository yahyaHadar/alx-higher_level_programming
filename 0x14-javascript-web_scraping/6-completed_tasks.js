#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 6-completed_tasks.js <api_url>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasks = tasks.filter(task => task.completed);
      const completedTasksByUser = completedTasks.reduce((result, task) => {
        if (result[task.userId]) {
          result[task.userId]++;
        } else {
          result[task.userId] = 1;
        }
        return result;
      }, {});

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
    }
  }
});
