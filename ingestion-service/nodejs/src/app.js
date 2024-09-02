import express from 'express';
import dotenv from 'dotenv';
import twitterRoutes from './routes/twitterRoutes.js';

// Load environment variables from .env file
dotenv.config();

const app = express();
app.use(express.json());

// Basic route
app.get('/', (req, res) => {
  res.send('Disaster Recovery Platform - Data Ingestion Service');
});

// Twitter routes
app.use('/api', twitterRoutes);

export default app;
