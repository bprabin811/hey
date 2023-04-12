// const followIcons = document.querySelectorAll('.follow a i');

// // Cache the window dimensions
// const windowHeight = window.innerHeight;
// const windowWidth = window.innerWidth;

// // Add hardware acceleration to icons
// followIcons.forEach((icon) => {
//   icon.style.transform = 'translate3d(0, 0, 0)';
// });

// function getRandomNumber(min, max) {
//   return Math.floor(Math.random() * (max - min) + min);
// }

// function moveIcon(icon) {
//   // Cache the current position of the icon
//   const currentPosition = icon.getBoundingClientRect();

//   // Generate random coordinates for the icon to move towards
//   const newX = getRandomNumber(0, windowWidth - 50);
//   const newY = getRandomNumber(0, windowHeight - 50);

//   // Define the animation function to move the icon towards the new position
//   function moveTowards() {
//     // Calculate the distance between the current position and the target position
//     const distanceX = newX - currentPosition.x;
//     const distanceY = newY - currentPosition.y;

//     // Calculate the amount of movement for each frame
//     const moveX = (distanceX / 5);
//     const moveY = (distanceY / 100);

//     // Move the icon by the calculated amount
//     icon.style.transform = `translate(${moveX}px, ${moveY}px)`;

//     // If the icon hasn't reached the target position, continue the animation
//     if (Math.abs(distanceX) > 1 || Math.abs(distanceY) > 1) {
//       requestAnimationFrame(moveTowards);
//     } else {
//       // If the icon has reached the target position, delay for 2 seconds and then return to the original position
//       setTimeout(() => {
//         returnToPosition();
//       }, 2000);
//     }
//   }

//   // Define the animation function to return the icon to its original position
//   function returnToPosition() {
//     // Cache the current position of the icon
//     const currentPosition = icon.getBoundingClientRect();

//     // Calculate the distance between the current position and the original position
//     const distanceX = 0 - currentPosition.x;
//     const distanceY = 0 - currentPosition.y;

//     // Move the icon by the calculated amount
//     icon.style.transform = `translate(${distanceX}px, ${distanceY}px)`;

//     // If the icon hasn't reached the original position, continue the animation
//     if (Math.abs(distanceX) > 1 || Math.abs(distanceY) > 1) {
//       requestAnimationFrame(returnToPosition);
//     }
//   }

//   // Start the animation to move the icon towards the new position
//   moveTowards();
// }

// function animateIcons(icons) {
//   icons.forEach((icon) => {
//     // Move the icon to a random position initially
//     moveIcon(icon);

//     // Every 5 seconds, move the icon to a new random position
//     setInterval(() => {
//       moveIcon(icon);
//     }, 2000);
//   });
// }

// animateIcons(followIcons);
