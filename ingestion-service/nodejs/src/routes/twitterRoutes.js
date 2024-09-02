import express from 'express';
import { getTweets } from '../controllers/twitterController.js';

const router = express.Router();

// Route for fetching tweets based on a keyword
router.get('/tweets', getTweets);

export default router;
