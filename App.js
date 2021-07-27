import React, { useState } from 'react';
import {
  Button,
  Linking,
  StyleSheet,
  Text,
  View,
} from 'react-native';


const App = () => {
  const [count, setCount] = useState(0);
  const onClickHandler = () => {
    setCount(count + 1);
  };

  return (
    <View style={styles.body}>
      <Text style={styles.text}>Counter: {count}</Text>
      <Button title='update state' onPress={onClickHandler}></Button>
    </View>
  );
};

const styles = StyleSheet.create({
  body: {
    flex: 1,
    backgroundColor: "#918fff",
    alignItems: 'center',
    justifyContent: 'center'
  },
  text: {

  }
});

export default App;
