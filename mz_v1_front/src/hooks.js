// src/hooks.js

export async function handle({ event, resolve }) {
  // 'maintenance' 페이지로의 요청을 제외하고 모두 리디렉션
  if (!event.url.pathname.startsWith('/maintenance')) {
    return Response.redirect(new URL('/maintenance', event.url), 302);
  }

  const response = await resolve(event);
  return response;
}
