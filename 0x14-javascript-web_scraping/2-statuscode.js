#!/usr/bin/node
import { get } from 'request';
get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
