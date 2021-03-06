function getCookie(name) {
    var cookieValue = null;
    if (document.cookie) {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteComment(id) {
    return fetch('/api/comments/delete/' + id + '/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        credentials: 'include'
    });
}

function createComment(formData) {
    return fetch('/api/comments/post/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}

function createArticle(formData) {
    return fetch('/api/articles/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}

function updateArticle(id, formData) {
    return fetch('/api/articles/' + id + '/', {
        method: 'PUT',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}

function uploadFile(formData) {
    return fetch('/imgbox/api/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}

function fetchDouban(doubanID) {
    return fetch('/api/tools/douban/?douban_id=' + doubanID, {
        method: 'GET',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        credentials: 'include'
    });
}

function createMonitorTask(formData) {
    return fetch('/api/monitor/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}

function verifyMonitorTask(formData) {
    return fetch('/api/monitor/verify/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
        credentials: 'include'
    });
}
