def test1a():
    cols = 13
    rows = 10000000
    raw_data = np.random.randint(2, size=(rows,cols))
    col_names = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07',
                 'v08', 'v09', 'v10', 'v11', 'v12', 'outcome']
    df = pd.DataFrame(raw_data, columns=col_names)
    df['v11'] = np.take(
        np.array(['t1', 't2', 't3', 't4'], dtype=object),
        np.random.randint(4, size=rows))
    df['v12'] = np.take(
        np.array(['p1', 'p2'], dtype=object),
        np.random.randint(2, size=rows))
    return df
