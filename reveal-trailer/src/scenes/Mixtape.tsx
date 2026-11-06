import {Sequence,useVideoConfig} from 'remotion';
import {Base,Plate,Title,Vinyl,Atmosphere,Flash,Insert} from '../design';
import {assets} from '../assets';
const Tag=({children}:{children:React.ReactNode})=><><Plate strength={.35}/><Vinyl x={1530} y={570} size={1100}/><Title align="left" size={145} top={310}>{children}</Title><Atmosphere/><Flash/></>;
export const Mixtape=()=>{const {fps}=useVideoConfig();return <Base><Sequence durationInFrames={60} premountFor={fps}><Tag>BUILD YOUR<br/>MIXTAPE.</Tag></Sequence><Sequence from={60} durationInFrames={60} premountFor={fps}><Tag>MASTER<br/>YOUR MOVES.</Tag></Sequence><Sequence from={120} durationInFrames={60} premountFor={fps}><Tag>CREATE<br/>YOUR LEGACY.</Tag></Sequence><Sequence from={180} durationInFrames={240} premountFor={fps}><Insert src={assets.menus} name="YOUR MIX. YOUR RULES." range="01:00–01:08" cue="Mixtape Studio / Ultimate Team / collection / deck building"/></Sequence></Base>};
