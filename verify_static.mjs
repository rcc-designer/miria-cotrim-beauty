import fs from 'node:fs';
import {siteContent as C} from './dist/siteContent.js';
import {videoContent as V} from './dist/videoContent.js';
const missing=[];
for(const route of [...C.routes,'/book/'])if(!fs.existsSync('dist'+route+'index.html'))missing.push(route);
for(let i=0;i<54;i++)for(const tail of ['.webp','-thumb.webp']){const path='dist/images/'+String(i).padStart(2,'0')+tail;if(!fs.existsSync(path))missing.push(path);}
for(const path of [V.desktop,V.mobile,V.poster])if(!fs.existsSync('dist'+path))missing.push(path);
if(missing.length)throw new Error(JSON.stringify(missing));
console.log('PASS: 10 route entrypoints, 108 image files, 2 video versions, poster and content configuration.');
