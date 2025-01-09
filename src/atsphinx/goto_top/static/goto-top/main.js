/**
 *
 */
document.addEventListener('DOMContentLoaded', () => {
  const template = document.getElementById('tmpl_gotoTop');
  const elm = template.content.cloneNode(true);
  elm.querySelector('button').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  document.body.appendChild(elm);
});
