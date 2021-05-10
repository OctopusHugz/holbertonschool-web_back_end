function handleResponseFromAPI(promise) {
  promise.then(() => ({ status: 200, body: 'success' })).then(() => {
    console.log('Got a response from the API');
  }).catch(() => Error());
}

export default handleResponseFromAPI;
