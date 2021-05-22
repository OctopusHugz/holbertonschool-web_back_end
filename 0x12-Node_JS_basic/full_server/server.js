import express from 'express';

const app = express();
const indexRouter = require('./routes/index');

const hostname = '127.0.0.1';
const port = 1245;

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
app.use('/', indexRouter);
app.use('/students', indexRouter);
app.use('/students/:major', indexRouter);

export default app;
