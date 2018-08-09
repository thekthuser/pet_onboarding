function toggle() { 
  var elems = document.getElementsByClassName('optional');
  var status = getComputedStyle(elems[0]).display;
  var style = '';
  if (status == 'none') {
    style = 'table-row';
  } else {
    stlye = 'none';
  }
  for (i = 0; i < elems.length; i++) {
    elems[i].style.display = style;
  }
};
