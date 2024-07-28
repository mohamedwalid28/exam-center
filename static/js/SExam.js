const cardData = [
    {
        heading:'Exam 1',
        body:'this is card body1'
    },
    {
        heading:'Exam 2',
        body:'this is card body2'
    },
    {
        heading:'Exam 3',
        body:'this is card body3'
    },
    {
        heading:'Exam 4',
        body:'this is card body4'
    },
    {
        heading:'Exam 5',
        body:'this is card body5'
    },
    {
        heading:'Exam 6',
        body:'this is card body6'
    },
    {
        heading:'Exam 7',
        body:'this is card body7'
    },
    {
        heading:'Exam 8',
        body:'this is card body8'
    },
]


{/* <h3 class="card-heading">card heading</h3>
<p class="card-body">this is card body</p> */}

const postContainer = document.querySelector('.card-container');

const postMethods = () => {
    cardData.map((postData) => {
        const postElement = document.createElement('div');
        postElement.classList.add('card');
        postElement.innerHTML = `
            <h3 class="card-heading">${postData.heading}</h3>
            <p class="card-body">${postData.body}</p>
            <button class="card-button" data-id="${postData.heading}">Apply</button>
        `;

        postContainer.appendChild(postElement);
    });

    // Add an event listener to the document that captures button clicks
    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('card-button')) {
            // Extract the data-id and data-heading attributes from the clicked button
            const buttonId = event.target.getAttribute('data-id');
            const buttonHeading = event.target.getAttribute('data-heading');

            // Redirect to the server route with the button information
            window.location.href = `/indexx`;
        }
    });
};

postMethods();