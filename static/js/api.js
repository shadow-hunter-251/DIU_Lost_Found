async function loadItems() {

    const container = document.getElementById(
        'api-items-container'
    );

    const emptyState = document.getElementById(
        'empty-state'
    );

    if (!container) {

        return;

    }


    /*
        Determine API URL
    */

    let apiURL = '/api/items/';


    if (window.location.pathname === '/items/lost/') {

        apiURL = '/api/items/?type=LOST';

    }


    if (window.location.pathname === '/items/found/') {

        apiURL = '/api/items/?type=FOUND';

    }


    /*
        Loading State
    */

    container.innerHTML = `

        <div class="col-span-full text-center py-12">

            <div class="text-slate-500">

                Loading items...

            </div>

        </div>

    `;


    /*
        Hide Empty State While Loading
    */

    if (emptyState) {

        emptyState.classList.add(
            'hidden'
        );

    }


    try {

        const response = await fetch(
            apiURL
        );


        if (!response.ok) {

            throw new Error(
                'Failed to load items.'
            );

        }


        const items = await response.json();


        /*
            Clear Loading State
        */

        container.innerHTML = '';


        /*
            Empty State
        */

        if (items.length === 0) {

            if (emptyState) {

                emptyState.classList.remove(
                    'hidden'
                );

            }

            return;

        }


        /*
            Hide Empty State
        */

        if (emptyState) {

            emptyState.classList.add(
                'hidden'
            );

        }


        /*
            Render Items
        */

        items.forEach(function (item) {

            const card = document.createElement(
                'div'
            );


            /*
                Card Design
            */

            card.className =
                'bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition';


            /*
                Image Fallback
            */

            let imageHTML;


            if (item.image) {

                imageHTML = `

                    <img
                        src="${item.image}"
                        alt="${item.title}"
                        class="w-full h-52 object-cover"
                        loading="lazy"
                    >

                `;

            } else {

                imageHTML = `

                    <div
                        class="w-full h-52 bg-slate-100 flex items-center justify-center"
                    >

                        <span class="text-slate-400">

                            No Image Available

                        </span>

                    </div>

                `;

            }


            /*
                LOST / FOUND Badge
            */

            let typeClass;


            if (item.item_type === 'LOST') {

                typeClass =
                    'bg-red-100 text-red-700';

            } else {

                typeClass =
                    'bg-green-100 text-green-700';

            }


            /*
                Item Card
            */

            card.innerHTML = `

                ${imageHTML}


                <div class="p-5">


                    <div class="flex items-center justify-between gap-3 mb-3">


                        <span
                            class="px-3 py-1 rounded-full text-xs font-semibold ${typeClass}"
                        >

                            ${item.item_type}

                        </span>


                        <span class="text-xs text-slate-500">

                            ${item.date}

                        </span>


                    </div>


                    <h3
                        class="text-lg font-bold text-slate-900 line-clamp-2"
                    >

                        ${item.title}

                    </h3>


                    <p
                        class="text-sm text-slate-600 mt-2 line-clamp-2"
                    >

                        ${item.description}

                    </p>


                    <div class="mt-4 space-y-2 text-sm text-slate-500">


                        <p>

                            📍 ${item.location}

                        </p>


                        <p>

                            🏷️ ${item.category_name || 'N/A'}

                        </p>


                    </div>


                    <a
                        href="/items/${item.id}/"
                        class="block text-center mt-5 bg-primary text-white py-2.5 rounded-lg font-semibold hover:opacity-90"
                    >

                        View Details

                    </a>


                </div>

            `;


            container.appendChild(
                card
            );

        });


    } catch (error) {


        /*
            Error State
        */

        container.innerHTML = `

            <div class="col-span-full text-center py-12">

                <p class="text-red-600">

                    Failed to load items.

                </p>

            </div>

        `;


        if (emptyState) {

            emptyState.classList.add(
                'hidden'
            );

        }


        console.error(
            error
        );

    }

}


loadItems();
