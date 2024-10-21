import React, { useEffect, useState } from 'react';
import { FlatList, Text, View, StyleSheet } from 'react-native';

interface NewsItem {
    title: string;
}

const App = () => {
    const [news, setNews] = useState<NewsItem[]>([]);

    useEffect(() => {
        fetch('URL_DEL_TUO_ENDPOINT_VERCEL/updates')
            .then(response => response.json())
            .then(data => setNews(data));
    }, []);

    return (
        <View style={styles.container}>
            <FlatList
                data={news}
                keyExtractor={(item) => item.title}
                renderItem={({ item }) => (
                    <Text style={styles.item}>{item.title}</Text>
                )}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        paddingTop: 50,
        backgroundColor: '#ecf0f1',
        padding: 8,
    },
    item: {
        padding: 10,
        fontSize: 18,
        height: 44,
    },
});

export default App;
