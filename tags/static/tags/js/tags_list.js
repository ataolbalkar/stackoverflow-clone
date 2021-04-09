$(document).ready(function () {
    const csrf = $('input[name=csrfmiddlewaretoken]')[0].value

    $('.tags-list-search-input').keydown(function () {  // On every keydown:
        setTimeout(function () {  // Wait for 1 sec before proceed.
            let value = $('.tags-list-search-input')[0].value;  // Take the input value.

            if (value === '') {  // If value is empty:
                $('#tag-browser').css('display', 'grid');  // Show the actual browser.
                $('#tag-browser-search').css('display', 'none');  // Hide the search browser.
                $('#tag-browser-search')[0].innerHTML = '';  // Clear the search browser.
            } else {
                // AJAX REQUEST
                $.ajax({
                    url: '',
                    type: 'POST',
                    data: {
                        value: value,
                        csrfmiddlewaretoken: csrf
                    },
                    // ON RESPONSE
                    success: function (response) {
                        $('#tag-browser').css('display', 'none');  // Hide the actual browser.
                        $('#tag-browser-search').css('display', 'grid');  // Show the search browser.
                        $('#tag-browser-search')[0].innerHTML = '';  // Clear the search browser.

                        let all_data = JSON.parse(response.data);  // Parse data as js object.

                        for (let i = 0; i < all_data.length; i++) {
                            all_data[i].count = response.counts[i];  // Add 'question counts' to the data objects.
                        }

                        for (data of all_data) {
                            // CREATE TAG ELEMENT:
                            let tag = document.createElement('div');
                            tag.className = 'tag';
                            tag.id = 'tag';

                            // Tag Name Elements:
                            let tag_name_area = document.createElement('div');
                            tag_name_area.className = 'tag-name-area';

                            let tag_name = document.createElement('a');
                            tag_name.className = 'tag-name';
                            tag_name.innerText = data.pk;
                            tag_name.href = '/tags/' + data.pk;

                            tag_name_area.appendChild(tag_name);
                            tag.appendChild(tag_name_area);

                            // Tag Info Elements:
                            let tag_info_area = document.createElement('div');
                            tag_info_area.className = 'tag-info-area';

                            let tag_info = document.createElement('span');
                            tag_info.className = 'tag-info';
                            tag_info.innerText = data.fields.info;

                            tag_info_area.appendChild(tag_info);
                            tag.appendChild(tag_info_area);

                            // Tag Statistics Elements:
                            let tag_statistics_area = document.createElement('div');
                            tag_statistics_area.className = 'tag-statistics-area';

                            let tag_statistics = document.createElement('span');
                            tag_statistics.className = 'tag-statistics';

                            // If count is 1, use the 'Question' keyword instead of 'Questions' to humanize:
                            let adv = ' Questions';
                            if (data.count === 1) {
                                adv = ' Question';
                            }
                            tag_statistics.innerText = data.count.toString() + adv;

                            tag_statistics_area.appendChild(tag_statistics);
                            tag.appendChild(tag_statistics_area);

                            $('#tag-browser-search')[0].appendChild(tag);  // Append the tag to the search browser.
                        }
                    }
                });
            }
        }, 1000);
    });
});