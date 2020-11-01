//Page Animation - Fade in and Out for soft transition//
function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}
document.addEventListener('DOMContentLoaded', function() {
    if (!window.AnimationEvent) { return; }
    var anchors = document.getElementsByTagName('a');
    for (var idx=0; idx<anchors.length; idx+=1) {
        if (anchors[idx].hostname !== window.location.hostname ||
            anchors[idx].pathname === window.location.pathname) {
            continue;
        }
    anchors[idx].addEventListener('click', function(event) {
        var fader = document.getElementById('fader'),
            anchor = event.currentTarget;
        
        var listener = function() {
            window.location = anchor.href;
            fader.removeEventListener('animationend', listener);
        };
            fader.addEventListener('animationend', listener);
            
            event.preventDefault();
            fader.classList.add('fade-in');
        });
    }
});

window.addEventListener('pageshow', function (event) {
    if (!event.persisted) {
        return;
    }
    var fader = document.getElementById('fader');
    fader.classList.remove('fade-in');
});

// Slideout Menu Interactivity //
const menuIcon = document.getElementById("menu-icon");
const slideoutMenu = document.getElementById("slideout-menu");

menuIcon.addEventListener('click', function() {
    if(slideoutMenu.style.opacity == "1") {
        slideoutMenu.style.opacity = "0";
        slideoutMenu.style.pointerEvents = 'none';
    } else {
        slideoutMenu.style.opacity = '1';
        slideoutMenu.style.pointerEvents = 'auto';
    }
});

slideoutMenu.addEventListener('click', function() {
    if(slideoutMenu.style.opacity == "1") {
        slideoutMenu.style.opacity ="0";
        slideoutMenu.style.pointerEvents ='none';
    }
});

// const searchIcon = document.getElementById("search-icon");
// const searchBox = document.getElementById("search-box");

// function rudrSwitchTab(rudr_tab_id, rudr_tab_content) {
// 	// first of all we get all tab content blocks (I think the best way to get them by class names)
// 	var x = document.getElementsByClassName("tabcontent");
// 	var i;
// 	for (i = 0; i < x.length; i++) {
// 		x[i].style.display = 'none'; // hide all tab content
// 	}
// 	document.getElementById(rudr_tab_content).style.display = 'block'; // display the content of the tab we need
 
// 	// now we get all tab menu items by class names (use the next code only if you need to highlight current tab)
// 	var x = document.getElementsByClassName("tabmenu");
// 	var i;
// 	for (i = 0; i < x.length; i++) {
// 		x[i].className = 'tabmenu'; 
// 	}
// 	document.getElementById(rudr_tab_id).className = 'tabmenu active';
// }

// searchIcon.addEventListener('click', function() {
//     if(searchBox.style.top == '2em') {
//         searchBox.style.top = '0px';
//         searchBox.style.pointerEvents = 'none';
//     } else {
//         searchBox.style.top = '2em';
//         searchBox.style.pointerEvents = 'auto';
//     }
// });

