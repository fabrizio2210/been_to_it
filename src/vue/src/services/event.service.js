var config = {};
config.apiUrl = window.location.origin;

export const eventService = {
  getEvent,
};

function getUid() {
  const requestOptions = {
    method: "GET",
  };

  return fetch(`${config.apiUrl}/api/event`, requestOptions).then(
    handleResponse
  );
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
