import App from './routes/main.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;