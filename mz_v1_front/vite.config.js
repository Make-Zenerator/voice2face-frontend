import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import dotenv from 'dotenv';

dotenv.config();

export default defineConfig({
	plugins: [sveltekit()],
	server: {
        fs: {
            allow: [
                '/Users/minyun/Documents/Code/Make-Zenerator/voice2face-frontend/mz_v1_front/_src_temp'
            ]
        }
    }
});
