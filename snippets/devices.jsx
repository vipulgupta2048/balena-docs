export const SupportedDevices = () => {
    const [devices, setDevices] = useState();

    useEffect(() => {
        (async () => {
            const response = await fetch('https://api.balena-cloud.com/v7/device_type?$select=name,slug,logo&$expand=is_of__cpu_architecture($select=slug)&$filter=is_default_for__application/any(idfa:((idfa/is_host%20eq%20true)%20and%20(idfa/is_archived%20eq%20false)%20and%20(idfa/owns__release/any(r:(status%20eq%20%27success%27)%20and%20(is_final%20eq%20true)%20and%20(is_invalidated%20eq%20false))))%20and%20not(contains(idfa/app_name,%27-esr%27)))&$orderby=name%20asc');
            const data = await response.json();
            setDevices(data.d);
        })();
    }, []);

    if (!devices) {
        return <i>loading</i>;
    }

    if (!devices.length) {
        return <i>No devices found</i>;
    }

    return (
        <table className="not-prose">
            <thead>
            <tr>
                <th></th>
                <th>Device name</th>
                <th>Slug</th>
                <th>Arch</th>
            </tr>
            </thead>
            <tbody>
            {devices.map((device) => (
                <tr>
                    <td><img src={device.logo} alt="" style={{ width: '60px', height: '60px' }} /></td>
                    <td>{device.name}</td>
                    <td><code>{device.slug}</code></td>
                    <td><code>{device.is_of__cpu_architecture[0]?.slug}</code></td>
                </tr>
            ))}
            </tbody>
        </table>
    )
}