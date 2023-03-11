var config = {};
config.apiUrl = window.location.origin;

export const photoService = {
  get,
  getAll,
  post,
};

function getAll() {
  const requestOptions = {
    method: "GET",
  };

  return fetch(`${config.apiUrl}/api/guests`, requestOptions).then(
    handleResponse
  );
}

function get(id) {
  const requestOptions = {
    method: "GET",
  };

  return fetch(`${config.apiUrl}/api/guest/${id}`, requestOptions).then(
    handleResponse
  );
}

function post(uid, photo) {
  var url = new URL(`/api/photo/${photo.id}`, config.apiUrl);
  const params = {
    author_id: uid,
  };
  const requestOptions = {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({
      author: photo.author,
      description: photo.description,
    }),
  };
  url.search = new URLSearchParams(params).toString();
  return fetch(url, requestOptions).then(handleResponse);
}

function handleResponse(response) {
  return response.text().then((text) => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }
    return data;
  });
}
