FRUIT=$1
if [ $FRUIT == APPLE ];then
	echo "You selected Apple!"
elif [ $FRUIT == ORANGE ];then
	echo "Yor selected Orange!"
elif [ $FRUIT == GRAPE ];then
	echo "you selected Grape!"
else
	echo "you selected other Fruit!"
fi
