#!/usr/bin/node
import { createWriteStream } from 'fs';
import request from 'request';
request(process.argv[2]).pipe(createWriteStream(process.argv[3]));
