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

function fadeMenu() {
    var slideoutMenu = document.getElementById("slideout-menu");
    if(slideoutMenu.style.display == "block") {
        slideoutMenu.style.display = "none";
        slideoutMenu.style.pointerEvents = 'none';
    } else {
        slideoutMenu.style.display = 'block';
        slideoutMenu.style.pointerEvents = 'auto';
    }
}
function MenuOn() {
    var slideoutMenu = document.getElementById("slideout-menu");
    if(slideoutMenu.style.display == "block") {
        slideoutMenu.style.display = "block";
        slideoutMenu.style.pointerEvents = 'auto';
    } else {
        slideoutMenu.style.display = 'block';
        slideoutMenu.style.pointerEvents = 'auto';
    }
}
function MenuOff() {
    var slideoutMenu = document.getElementById("slideout-menu");
    if(slideoutMenu.style.display == "block") {
        slideoutMenu.style.display = "none";
        slideoutMenu.style.pointerEvents = 'none';
    } else {
        slideoutMenu.style.display = 'none';
        slideoutMenu.style.pointerEvents = 'none';
    }
}
// menuIcon.addEventListener('click', function() {
//     if(slideoutMenu.style.opacity == "1") {
//         slideoutMenu.style.opacity = "0";
//         slideoutMenu.style.pointerEvents = 'none';
//     } else {
//         slideoutMenu.style.opacity = '1';
//         slideoutMenu.style.pointerEvents = 'auto';
//     }
// });

// slideoutMenu.addEventListener('click', function() {
//     if(slideoutMenu.style.opacity == "1") {
//         slideoutMenu.style.opacity ="0";
//         slideoutMenu.style.pointerEvents ='none';
//     }
// });