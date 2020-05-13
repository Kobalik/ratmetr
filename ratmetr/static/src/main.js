const table_div = document.getElementsByClassName('tablrat');
const right_panel_div = document.getElementsByClassName('rightpanel');

const height = table_div.offsetHeight;

right_panel_div.style.height = height + 'px';

console.log(table_div.offsetHeight);
console.log(right_panel_div.offsetHeight);