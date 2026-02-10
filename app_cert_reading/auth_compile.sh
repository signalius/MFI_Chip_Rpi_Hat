gcc $(pkg-config --cflags glib-2.0) -o auth.out auth.c $(pkg-config --libs glib-2.0)

