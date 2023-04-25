#!/usr/bin/node
import { writeFile } from 'fs';
writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
