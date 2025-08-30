import { Hono } from 'hono'
const app = new Hono()
app.get('/health', c => c.json({status:'ok'}))
app.get('/tools/example1', c => c.json({tool:'example1', result:{message:'hello', project:'ProjectA'}}))
app.get('/tools/example2', c => c.json({tool:'example2', result:{count:2, items:['alpha','beta']}}))
export default app
if (process.env.NODE_ENV !== 'test') {
  const http = await import('node:http')
  const port = Number(process.env.PORT || 8787)
  const server = http.createServer((req, res) => {
    app.fetch(req as any, { env: process.env } as any).then(r => {
      res.writeHead(r.status, Object.fromEntries(r.headers.entries()))
      r.arrayBuffer().then(buf => res.end(Buffer.from(buf)))
    }).catch(err => { res.statusCode=500; res.end(String(err)) })
  }); server.listen(port, () => console.log(`listening on http://localhost:${port}`))
}
