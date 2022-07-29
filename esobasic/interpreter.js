const fs = require("fs");
const readline = require("readline-sync");

function readFile(filename) {
  return fs.readFileSync(filename).toString();
}

function get_subarray(arr, start) {
  text = "";

  while (start < arr.length) {
    text += arr[start];
    start++;
  }

  return text;
}

function find_var(arr, name) {
  for (let i in arr) {
    if (arr[i].var_name == name) {
      return arr[i].var_val;
    }
  }
  throw new Error('No var found');
}

function find_var_index(arr, name) {
  for (let i in arr) {
    if (arr[i].var_name == name) {
      return i;
    }
  }
}

function interpret() {
  const filename = "hello.esobasic";
  const code = readFile(filename);

  lines = code.replaceAll("\r", '').split("\n");
  stack = [];

  let i = 0

  while (i < lines.length) {
    line = lines[i];
    broken = line.split(' ');

    if (line == 'CLS') {
      console.clear();
    } else if (broken[0] == 'PRINT') {
      console.log(get_subarray(broken, 1));
    } else if (line == 'END') {
      return;
    } else if (broken[0] == 'PRINTVAR') {
      console.log(find_var(stack, broken[1]));
    } else if (broken[0] == 'LET') {
      if (broken.length == 2) {
        stack.push({var_name: broken[1], var_val: 0});
      } else if (broken[1] == '-=') {
        stack[find_var_index(stack, broken[2])].var_val--;
      } else if (broken[1] == '+=') {
        stack[find_var_index(stack, broken[2])].var_val++;
      }
    } else if (broken[0] == 'INPUT') {
      stack.push({var_name: broken[1], var_val: readline.question()});
    } else if (broken[0] == 'GOTO') {
      i = Number(broken[1]) - 1;
    } else if (broken[0] == 'IF') {
      if(find_var(stack, broken[1]) == 0) {
        i = i + 1;
      }
    }

    i = i + 1;
  }
}

interpret();