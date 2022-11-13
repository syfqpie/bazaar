# Bazaar - Marketplace Webapp 🛒

> A bazaar (Persian: بازار) or souk (Arabic: سوق, romanized: sūq; also transliterated as souq)
> is a marketplace consisting of multiple small stalls or shops, especially in the Middle East,
> North Africa, and India.

## Project Setup

```sh
yarn
```

### Add environment variables
Create a .env file in ./web and add this default variables

```sh
VITE_APP_ENV=development
VITE_BASE_URL=http://127.0.0.1:8000/
```

### Compile and Hot-Reload for Development

```sh
yarn dev
```

### Type-Check, Compile and Minify for Production

```sh
yarn build
```

### Run Unit Tests with Vitest

```sh
yarn test:unit
```

### Lint with ESLint
```sh
yarn lint
```

## References
- [Vite Configuration Reference](https://vitejs.dev/config/)
- [Vitest](https://vitest.dev/)
- [ESLint](https://eslint.org/)