/* Inline SVG icon set (stroke-based, 24px viewBox). Keeps the hub self-contained
   with no icon-font dependency. */
const P = 'stroke="currentColor" stroke-width="1.7" fill="none" stroke-linecap="round" stroke-linejoin="round"';
const wrap = (inner) => `<svg viewBox="0 0 24 24" aria-hidden="true">${inner}</svg>`;

export const icon = {
  home: () => wrap(`<path ${P} d="M3 10.5 12 3l9 7.5"/><path ${P} d="M5 9.5V20h14V9.5"/><path ${P} d="M9.5 20v-6h5v6"/>`),
  back: () => wrap(`<path ${P} d="M15 5l-7 7 7 7"/>`),
  forward: () => wrap(`<path ${P} d="M9 5l7 7-7 7"/>`),
  chevron: () => wrap(`<path ${P} d="M9 6l6 6-6 6"/>`),
  sessions: () => wrap(`<rect ${P} x="3" y="4" width="18" height="16" rx="2"/><path ${P} d="M3 9h18M8 4v16"/>`),
  rubric: () => wrap(`<rect ${P} x="4" y="3" width="16" height="18" rx="2"/><path ${P} d="M8 8h8M8 12h8M8 16h5"/>`),
  analytics: () => wrap(`<path ${P} d="M4 20V4M20 20H4"/><path ${P} d="M8 16l3-4 3 2 4-6"/>`),
  raters: () => wrap(`<circle ${P} cx="9" cy="8" r="3"/><path ${P} d="M3 20c0-3 3-5 6-5s6 2 6 5"/><path ${P} d="M16 4a3 3 0 010 8M21 20c0-2.5-1.5-4-4-5"/>`),
  report: () => wrap(`<path ${P} d="M6 3h9l3 3v15H6z"/><path ${P} d="M14 3v4h4"/><path ${P} d="M9 13h6M9 17h6"/>`),
  score: () => wrap(`<path ${P} d="M12 3l2.6 5.6 6 .6-4.5 4 1.3 6L12 16.6 6.6 19.2l1.3-6-4.5-4 6-.6z"/>`),
  settings: () => wrap(`<circle ${P} cx="12" cy="12" r="3"/><path ${P} d="M19 12a7 7 0 00-.1-1l2-1.5-2-3.4-2.3 1a7 7 0 00-1.7-1l-.3-2.5h-4l-.3 2.5a7 7 0 00-1.7 1l-2.3-1-2 3.4 2 1.5a7 7 0 000 2l-2 1.5 2 3.4 2.3-1a7 7 0 001.7 1l.3 2.5h4l.3-2.5a7 7 0 001.7-1l2.3 1 2-3.4-2-1.5a7 7 0 00.1-1z"/>`),
  search: () => wrap(`<circle ${P} cx="11" cy="11" r="7"/><path ${P} d="M21 21l-4-4"/>`),
  menu: () => wrap(`<path ${P} d="M4 7h16M4 12h16M4 17h16"/>`),
  plus: () => wrap(`<path ${P} d="M12 5v14M5 12h14"/>`),
  check: () => wrap(`<path ${P} d="M20 6L9 17l-5-5"/>`),
  info: () => wrap(`<circle ${P} cx="12" cy="12" r="9"/><path ${P} d="M12 11v5M12 8h.01"/>`),
  flag: () => wrap(`<path ${P} d="M5 21V4M5 4h11l-2 3 2 3H5"/>`),
  arrowUp: () => wrap(`<path ${P} d="M12 19V5M5 12l7-7 7 7"/>`),
  arrowDown: () => wrap(`<path ${P} d="M12 5v14M5 12l7 7 7-7"/>`),
  arrowRight: () => wrap(`<path ${P} d="M5 12h14M13 6l6 6-6 6"/>`),
  clock: () => wrap(`<circle ${P} cx="12" cy="12" r="9"/><path ${P} d="M12 7v5l3 2"/>`),
  users: () => wrap(`<circle ${P} cx="9" cy="8" r="3"/><path ${P} d="M3 20c0-3 3-5 6-5s6 2 6 5"/>`),
  lock: () => wrap(`<rect ${P} x="5" y="11" width="14" height="9" rx="2"/><path ${P} d="M8 11V8a4 4 0 018 0v3"/>`),
  target: () => wrap(`<circle ${P} cx="12" cy="12" r="9"/><circle ${P} cx="12" cy="12" r="5"/><circle ${P} cx="12" cy="12" r="1.4"/>`),
  logo: () => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3c0 5 4 6 4 9s-2 4-2 6" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M18 3c0 5-4 6-4 9s2 4 2 6" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity=".85"/><circle cx="12" cy="20" r="1.6" fill="#fff"/></svg>`,
};
