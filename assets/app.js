const weeks=[
 {n:"Week 1",title:"Make timing visible",posts:[["Instagram carousel","Warum die Stunde zählt"],["LinkedIn document","Flexibility without the jargon"],["Vertical video","One appliance, one better hour"]]},
 {n:"Week 2",title:"Build understanding",posts:[["Instagram carousel","Welche Geräte sind flexibel?"],["LinkedIn single image","Nicht jeder Tarif belohnt Verschiebung"],["Stories poll","Wann läuft deine Spülmaschine?"]]},
 {n:"Week 3",title:"Enable one action",posts:[["Instagram carousel","A four-step flexibility check"],["LinkedIn chart","Why timing and infrastructure meet"],["Vertical video","In 30 Sekunden geplant"]]},
 {n:"Week 4",title:"Reflect with trust",posts:[["Instagram carousel","Was hat funktioniert?"],["LinkedIn document","What we can and cannot claim"],["Cross-channel wrap","Eine bessere Stunde beginnt klein"]]}
];
document.getElementById("weeks").innerHTML=weeks.map(w=>`<article class="week"><strong>${w.n}</strong><h3>${w.title}</h3>${w.posts.map(p=>`<div class="post"><b>${p[1]}</b><span>${p[0]}</span></div>`).join("")}</article>`).join("");
