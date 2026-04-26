// LOADER
window.addEventListener('load',()=>setTimeout(()=>document.getElementById('loader').classList.add('out'),2400));

// NAV
window.addEventListener('scroll',()=>document.getElementById('nav').classList.toggle('sc',scrollY>50));

// MOBILE MENU
function toggleMob(){document.getElementById('mmenu').classList.toggle('open')}
function closeMob(){document.getElementById('mmenu').classList.remove('open')}

// TYPING
const words=['Python Developer','Django Expert','Full Stack Developer','REST API Builder','WordPress Developer','Problem Solver'];
let wi=0,ci2=0,del=false;
const tw=document.getElementById('tword');
function type(){
  const w=words[wi];
  if(!del){ci2++;tw.textContent=w.slice(0,ci2);if(ci2===w.length){del=true;setTimeout(type,2000);return}}
  else{ci2--;tw.textContent=w.slice(0,ci2);if(ci2===0){del=false;wi=(wi+1)%words.length;setTimeout(type,400);return}}
  setTimeout(type,del?50:90);
}
setTimeout(type,2600);

// SCROLL REVEAL + SKILL BARS
const obs=new IntersectionObserver(en=>{
  en.forEach(e=>{
    if(e.isIntersecting){
      e.target.classList.add('v');
      e.target.querySelectorAll('.sk-fill').forEach(f=>f.style.width=f.dataset.w+'%');
    }
  });
},{threshold:0.1});
document.querySelectorAll('.rev,.rev-l,.rev-r').forEach(el=>obs.observe(el));

// CSRF Token helper
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// CONTACT FORM
function sendMsg(e){
  e.preventDefault();
  const btn=e.target.querySelector('button');
  btn.textContent='Sending...';
  
  const formData = new FormData(e.target);
  const data = {
    name: formData.get('name') || e.target.querySelector('input[type="text"]').value,
    email: formData.get('email') || e.target.querySelector('input[type="email"]').value,
    subject: formData.get('subject') || e.target.querySelectorAll('input[type="text"]')[1].value,
    message: formData.get('message') || e.target.querySelector('textarea').value,
  };
  
  fetch('/api/contact/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(data => {
    btn.textContent='Send Message →';
    const s=document.getElementById('fsuccess');
    s.style.display='block';
    e.target.reset();
    setTimeout(()=>s.style.display='none',6000);
  })
  .catch(err => {
    btn.textContent='Send Message →';
    console.error(err);
    alert('Something went wrong. Please try again.');
  });
}

// Skill hover — 0 se % tak animation
function animSkill(item) {
  const fill = item.querySelector('.sk-fill');
  const w = item.dataset.w;

  // Pehle 0 pe le jao (fast)
  item.classList.add('resetting');
  fill.style.width = '0%';

  // Phir thodi der baad % tak jao (smooth)
  setTimeout(() => {
    item.classList.remove('resetting');
    fill.style.width = w + '%';
  }, 350);
}

