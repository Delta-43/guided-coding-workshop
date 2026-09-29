const form = document.querySelector('#search-form');
const input = document.querySelector('#city');
const button = document.querySelector('#search-button');
const status = document.querySelector('#status');
const statusText = document.querySelector('#status-text');
const weather = document.querySelector('#weather');
let requestController;

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const city = input.value.trim();
  if (!city) {
    input.focus();
    return;
  }

  requestController?.abort();
  const controller = new AbortController();
  requestController = controller;
  weather.hidden = true;
  status.hidden = false;
  status.classList.remove('error');
  status.classList.add('loading');
  statusText.textContent = 'Checking conditions…';
  button.disabled = true;

  try {
    const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`, {
      signal: controller.signal,
    });
    const data = await response.json();
    if (!response.ok) throw new Error(typeof data.detail === 'string' ? data.detail : 'Could not load weather');

    document.querySelector('#place').textContent = [data.city, data.country].filter(Boolean).join(', ');
    document.querySelector('#observed').textContent = `Updated ${data.observed_at.replace('T', ' ')} local time`;
    document.querySelector('#icon').textContent = data.icon;
    document.querySelector('#temperature').textContent = Math.round(data.temperature);
    document.querySelector('#condition').textContent = data.condition;
    document.querySelector('#feels-like').textContent = `${Math.round(data.feels_like)}°C`;
    document.querySelector('#humidity').textContent = `${data.humidity}%`;
    document.querySelector('#wind').textContent = `${Math.round(data.wind_speed)} km/h`;
    status.hidden = true;
    weather.hidden = false;
    weather.focus();
  } catch (error) {
    if (error.name === 'AbortError') return;
    statusText.textContent = error instanceof TypeError ? 'Could not connect. Please try again.' : error.message;
    status.classList.add('error');
  } finally {
    if (requestController === controller) {
      status.classList.remove('loading');
      button.disabled = false;
    }
  }
});