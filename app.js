const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controlls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelectorAll('.main-content');
// console.log(sectBtn.length);

function PageTransition() {
    for (let i = 0; i < sectBtn.length; i++) {
        sectBtn[i].addEventListener('click', function () {
            let currentBtn = document.querySelectorAll('.active-btn');
            currentBtn[0].className = currentBtn[0].className.replace('active-btn', '');
            this.className += ' active-btn';
        })
    }

    //Sections Active class
    allSections.forEach((section) =>
        section.addEventListener("click", (e) => {
            const id = e.target.dataset.id;
            // console.log(id);

            if (id) {
                sectBtns.forEach((btn) => {
                    btn.classList.remove("active");
                });
                e.target.classList.add("active");
                sections.forEach((section) => {
                    section.classList.remove("active");
                });

                const element = document.getElementById(id);
                console.log(element);
                element.classList.add("active");
            }
        })
    );
}

PageTransition();