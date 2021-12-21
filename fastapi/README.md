I'll get to this shortly.

## Deploying

Once the app is ready for production, copy the files to your server. 

Using a daemon manager is a good practice, but I'm not doing that here.

```bash
nohup python ./main.py > /var/log/todo.log &
```
