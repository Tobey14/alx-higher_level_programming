#!/usr/bin/node
import { readFile } from 'fs';
readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
