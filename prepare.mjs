import fs from 'node:fs';
import {seo} from './dist/seo.js';
const routes=['about','services','bridal','portfolio','academy','shop','journal','contact','book'];
let html=fs.readFileSync('dist/index.html','utf8');
if(!html.includes('components.css'))html=html.replace('</head>','<link rel="stylesheet" href="/components.css"></head>');
if(!html.includes('video.css'))html=html.replace('</head>','<link rel="stylesheet" href="/video.css"></head>');
const entry=(route)=>html.replace(/<title>.*?<\/title>/,`<title>${seo.routes[route]} | ${seo.brand}</title>`).replace(/<meta name="description" content="[^"]*">/,`<meta name="description" content="${seo.description}">`).replace(/<script type="application\/ld\+json">.*?<\/script>/,'').replace('</head>',`<script type="application/ld+json">${JSON.stringify(seo.person)}</script></head>`);
fs.writeFileSync('dist/index.html',entry('home'));
for(const route of routes){fs.mkdirSync(`dist/${route}`,{recursive:true});fs.writeFileSync(`dist/${route}/index.html`,entry(route));}
console.log('10 routes prepared.');
