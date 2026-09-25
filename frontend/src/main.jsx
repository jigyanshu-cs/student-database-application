import React,{useEffect,useState}from'react';
import{createRoot}from'react-dom/client';
import'./style.css';

const API=import.meta.env.VITE_API_URL||'http://localhost:8000';

function App(){
const[t,setT]=useState(localStorage.getItem('token')||''),
[l,setL]=useState({email:'',password:''}),
[s,setS]=useState([]),
[q,setQ]=useState(''),
[a,setA]=useState(''),
[editing,setEditing]=useState(null),
[f,setF]=useState({name:'',email:'',course:'BTech CSE',year:2,cgpa:'',phone:''});

async function login(e){
e.preventDefault();
let r=await fetch(API+'/api/auth/login-json',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify(l)
});
let d=await r.json();
if(r.ok){
localStorage.setItem('token',d.access_token);
setT(d.access_token)
}else alert(d.detail)
}

async function load(){
let r=await fetch(API+'/api/students/',{
headers:{Authorization:'Bearer '+t}
});
if(r.ok)setS(await r.json())
}

useEffect(()=>{
if(t)load()
},[t]);

async function add(e){
e.preventDefault();

let url=editing
?API+'/api/students/'+editing
:API+'/api/students/';

let method=editing?'PUT':'POST';

let r=await fetch(url,{
method:method,
headers:{
'Content-Type':'application/json',
Authorization:'Bearer '+t
},
body:JSON.stringify({
...f,
year:+f.year,
cgpa:f.cgpa?+f.cgpa:null
})
});

if(r.ok){
setF({
name:'',
email:'',
course:'BTech CSE',
year:2,
cgpa:'',
phone:''
});
setEditing(null);
load();
}else{
let d=await r.json();
alert(d.detail||'Operation failed');
}
}

function editStudent(x){
setEditing(x.id);

setF({
name:x.name,
email:x.email,
course:x.course,
year:x.year,
cgpa:x.cgpa??'',
phone:x.phone??''
});

window.scrollTo({
top:0,
behavior:'smooth'
});
}

function cancelEdit(){
setEditing(null);

setF({
name:'',
email:'',
course:'BTech CSE',
year:2,
cgpa:'',
phone:''
});
}

async function removeStudent(id){
if(!window.confirm('Are you sure you want to delete this student?'))return;

let r=await fetch(API+'/api/students/'+id,{
method:'DELETE',
headers:{
Authorization:'Bearer '+t
}
});

if(r.ok){
load()
}else{
let d=await r.json();
alert(d.detail||'Failed to delete student');
}
}

async function chat(e){
e.preventDefault();

let r=await fetch(API+'/api/chatbot/chat',{
method:'POST',
headers:{
'Content-Type':'application/json',
Authorization:'Bearer '+t
},
body:JSON.stringify({message:q})
});

let d=await r.json();
setA(d.response||d.detail)
}

if(!t)
return <main className="center">
<form className="card"onSubmit={login}>
<h1>Student Portal</h1>

<label>Email</label>
<input
type="email"
placeholder="Enter your email"
value={l.email}
onChange={e=>setL({...l,email:e.target.value})}
required
/>

<label>Password</label>
<input
type="password"
placeholder="Enter your password"
value={l.password}
onChange={e=>setL({...l,password:e.target.value})}
required
/>

<button>Login</button>
</form>
</main>;

return <main>

<header>
<h1>Student Database System</h1>

<button onClick={()=>{
localStorage.removeItem('token');
setT('')
}}>
Logout
</button>
</header>

<div className="grid">

<form className="card"onSubmit={add}>

<h2>{editing?'Edit Student':'Add Student'}</h2>

{['name','email','course','year','cgpa','phone'].map(k=>
<input
key={k}
placeholder={k}
value={f[k]}
onChange={e=>setF({...f,[k]:e.target.value})}
required={['name','email','course','year'].includes(k)}
/>
)}

<button>
{editing?'Update Student':'Add Student'}
</button>

{editing&&
<button
type="button"
onClick={cancelEdit}
>
Cancel
</button>
}

</form>

<form className="card"onSubmit={chat}>
<h2>AI Assistant</h2>

<textarea
value={q}
onChange={e=>setQ(e.target.value)}
placeholder="Find students in BTech CSE..."
/>

<button>Ask Gemini</button>

<p>{a}</p>
</form>

</div>

<section className="card">

<h2>Students</h2>

<table>

<thead>
<tr>
<th>ID</th>
<th>Name</th>
<th>Email</th>
<th>Course</th>
<th>Year</th>
<th>CGPA</th>
<th>Action</th>
</tr>
</thead>

<tbody>

{s.map(x=>
<tr key={x.id}>

<td>{x.id}</td>
<td>{x.name}</td>
<td>{x.email}</td>
<td>{x.course}</td>
<td>{x.year}</td>
<td>{x.cgpa??'-'}</td>

<td>

<button
type="button"
onClick={()=>editStudent(x)}
>
Edit
</button>

<button
type="button"
onClick={()=>removeStudent(x.id)}
>
    Delete
    </button>
    </td>
    </tr>
)}
</tbody>
</table>
</section>
</main>
}
createRoot(document.getElementById('root')).render(<App/>);