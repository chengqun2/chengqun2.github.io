const { CronJob } = require('cron');

/*
* * * * * *: Runs every second
0 * * * * *: Runs at the start of every minute
0 0 * * * *: Runs at the start of every hour
0 0 9 * * *: Runs every day at 9 AM
*/
const job = new CronJob('0 * * * * *', () => {
  console.log('This runs every minute!');
});

// Start the cron job
job.start();
